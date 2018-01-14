import pyaudio
import wave

def record_wav(channels, rate, seconds, 
               file_path, _format=pyaudio.paInt16,
               chunk_size=1000):
    """
            Records *.wav file with specified params 
        and saves it to file.

        :param channels: int
        :param rate: int
        :param seconds: int
        :param file_path: str
            Path to file to save audio in.
        :param _format: int
            Size of frame.
        :param chunk_size: int


        :return: None
    """

    p = pyaudio.PyAudio()

    stream = p.open(format=_format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk_size)

    print("* recording")

    frames = []

    for i in range(0, int(rate / chunk_size * seconds)):
        data = stream.read(chunk_size)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(file_path, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(_format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

if __name__ == '__main__':
    record_wav(1, 16000, 1, 'output.wav')
