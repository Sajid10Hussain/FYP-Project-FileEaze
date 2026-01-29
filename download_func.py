from pytube import YouTube
import time

def downloader(url, save_path, format_selected, quality_selected, progress_callback, alert_callback, size_callback, speed_callback, time_callback, is_paused, is_canceled, status_callback, error_callback):
    yt = YouTube(url)
    stream = None

    try:
        if format_selected == 'Video':
            if quality_selected == '360p':
                stream = yt.streams.filter(progressive=True, file_extension='mp4', resolution='360p').first()
            elif quality_selected == '720p':
                stream = yt.streams.filter(progressive=True, file_extension='mp4', resolution='720p').first()
            else:
                stream = yt.streams.filter(progressive=True, file_extension='mp4', resolution='1080p').first()
        elif format_selected == 'Audio':
            if quality_selected == '128kbps':
                stream = yt.streams.filter(only_audio=True, abr='128kbps').first()
            elif quality_selected == '256kbps':
                stream = yt.streams.filter(only_audio=True, abr='256kbps').first()
            else:
                stream = yt.streams.filter(only_audio=True, abr='320kbps').first()
        
        if stream is None:
            raise Exception("No suitable stream found for the selected format and quality.")

        start_time = time.time()
        total_size = stream.filesize
        status_callback("File receiving")

        def on_progress(stream, chunk, bytes_remaining):
            nonlocal total_size
            bytes_downloaded = total_size - bytes_remaining
            progress = int((bytes_downloaded / total_size) * 100)
            progress_callback(progress)
            size_callback(total_size)

            elapsed_time = time.time() - start_time
            time_callback(elapsed_time)

            speed = bytes_downloaded / elapsed_time if elapsed_time > 0 else 0
            speed_callback(speed)

            while is_paused():
                time.sleep(0.1)
                status_callback("Paused")
            if is_canceled():
                status_callback("Canceled")
                raise Exception("Download canceled")

        yt.register_on_progress_callback(on_progress)

        if stream:
            stream.download(output_path=save_path)
            status_callback("Download completed")
            alert_callback()
    except Exception as e:
        print(f"Error during download: {e}")
        status_callback("Download failed")
        error_callback(f"Download failed: {e}")
