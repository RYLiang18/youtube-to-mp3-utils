# !/bin/zsh

# ask for playlist URL
echo Hello, give me the URL to your playlist:
read playlist_url

# ask for filename to save all the URL strings of the playlist
echo Enter a filename that I should save the playlist URLs into \(just type a filename, not a path to a file\):
read playlist_filename

# building image and running the container
docker build -t playlist_parser_image .
docker run -v playlist-volume:/home/appuser/playlist --name playlist_parser_container playlist_parser_image $playlist_url $playlist_filename.txt

# cleaning up the image and container
docker container rm playlist_parser_container
docker image rm playlist_parser_image:latest

echo ======== fin ========
echo you can find your file in the named docker volume \"playlist-volume\"
echo please delete the volume after copying its contents with: \"docker volume rm playlist-volume\"

