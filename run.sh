# !/bin/zsh

docker build -t giich_youtube_to_mp3_image .
docker run -it -v mp3-volume:/home/appuser/playlist --name giich_youtube_to_mp3_container giich_youtube_to_mp3_image:latest

echo "cleaning up..."
docker container rm giich_youtube_to_mp3_container
docker image rm giich_youtube_to_mp3_image:latest
echo "======== fin ========"
echo you can find your file in the named docker volume \"mp3-volume\"
echo please delete the volume after moving out its contents with: \"docker volume rm mp3-volume\"