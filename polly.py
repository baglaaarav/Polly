import boto3
polly = boto3.client('polly',region_name='us-east-1',aws_access_key_id='AKIAUQPJ7O66JJVACKT6',aws_secret_access_key='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')
text="we are using amazon polly outside the aws where it can be used in the busness logics"

response = polly.synthesize_speech(Text=text, OutputFormat="mp3",
                                    VoiceId="Aditi")
if "AudioStream" in response:
        with response["AudioStream"] as stream:
           output_file = "speech.mp3"
           try:
            # Open a file for writing the output as a binary stream
                with open(output_file, "wb") as file:
                   file.write(stream.read())
           except IOError as error:
              # Could not write to file, exit gracefully
              print(error)
else:
    # The response didn't contain audio data, exit gracefully
    print("Could not stream audio")
    
    

from IPython.display import Audio
Audio(output_file, autoplay=True)