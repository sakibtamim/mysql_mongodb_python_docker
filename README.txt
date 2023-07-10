1. first build a mongo image
2. then run with "docker run -d -p 27017:27017 --name mongodb mongo"
3. reusing the above container "docker start mongodb'(container-name/image)'"
4. stop a container "docker stop mongodb(conaiter-name/immage)"