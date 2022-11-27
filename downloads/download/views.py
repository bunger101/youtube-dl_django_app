from django.http import HttpResponse
from django.shortcuts import render
import youtube_dl
from .forms import DownloadForm
import re

# Create your views here.

def homepage(request):
    return render(request, 'download/home1.html')

def Dmp4(request):
    global context
    form = DownloadForm(request.POST or None)

    if form.is_valid():
        video_url = form.cleaned_data.get("url")
        regex = r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+'
        print(video_url)
        if not re.match(regex, video_url):
            return HttpResponse('Introduce a correct URL.\
                Please at the main page.')

        ydl_opts = {}
        
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(
                video_url, download=False)
        video_audio_streams = []
        for m in meta['formats']: #type: ignore
            file_size = m['filesize']
            if file_size is not None:
                file_size = f'{round(int(file_size) / 1000000,2)} Mb'
            else:
                pass
            resolution = 'Audio'
            if m['height'] is not None:
                resolution = f"{m['height']} x {m['width']}"
            video_audio_streams.append({
                'resolution': resolution,
                'extension': m['ext'],
                'file_size': file_size,
                'video_url': m['url']
            })
            if resolution == 'Audio':
                video_audio_streams.remove({
                'resolution': resolution,
                'extension': m['ext'],
                'file_size': file_size,
                'video_url': m['url']
            })
            if file_size is None:
                video_audio_streams.remove({
                'resolution': resolution,
                'extension': m['ext'],
                'file_size': file_size,
                'video_url': m['url']
            })
        
        video_audio_streams = video_audio_streams[::-1]
        context = {
            'form': form,
            'title': meta['title'], #type: ignore
            'streams': video_audio_streams,
            'duration': round(int(meta['duration'])/60, 2), #type: ignore
            'views': f'{int(meta["view_count"]):,}', #type: ignore
            'thumb': meta['thumbnails'][3]['url'], #type: ignore
        }
        
        return render(request, 'download/home2.html', context)
    return render(request, 'download/home2.html', {'form': form})

def Dmp3(request):
    global context
    form = DownloadForm(request.POST or None)

    if form.is_valid():
        video_url = form.cleaned_data.get("url")
        regex = r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+'
        print(video_url)
        if not re.match(regex, video_url):
            return HttpResponse('Introduce a correct URL.\
                Please at the main page.')
            
        ydl_opts = {}
        
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(
                video_url, download=False)
        video_audio_streams = []
        for m in meta['formats']: #type: ignore
            file_size = m['filesize']
            if file_size is not None:
                file_size = f'{round(int(file_size) / 1000000,2)} Mb'
            resolution = 'Audio'
            if m['height'] is not None:
                resolution = f"{m['height']} x {m['width']}"
            video_audio_streams.append({
                'resolution': resolution,
                'extension': m['ext'],
                'file_size': file_size,
                'video_url': m['url']
            })
            if resolution != 'Audio':
                video_audio_streams.remove({
                'resolution': resolution,
                'extension': m['ext'],
                'file_size': file_size,
                'video_url': m['url']
            })
        
        video_audio_streams = video_audio_streams[::-1]
        context = {
            'form': form,
            'title': meta['title'], #type: ignore
            'streams': video_audio_streams,
            'duration': round(int(meta['duration'])/60, 2), #type: ignore
            'views': f'{int(meta["view_count"]):,}', #type: ignore
            'thumb': meta['thumbnails'][3]['url'], #type: ignore
        }
        
        return render(request, 'download/home3.html', context)
    return render(request, 'download/home3.html', {'form': form})
