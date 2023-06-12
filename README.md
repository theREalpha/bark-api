# bark-api
A docker enabled fastAPI endpoint for processing prompt using bark and returning results


# setup
docker build -t bark-api .<br>
docker run -d -p 15320:15320 bark-api

# Description
The app runs on localhost port 15320, and listens for POST requests at '/process-prompt' endpoint to generate wav file using bark module and returns the wav file as a response.<br>
The prompt is sent as part of the payload of POST Request :
    {"prompt": "text-here"}
    
# Testing Example
curl -X POST -H "Content-Type: application/json" -d {"prompt": "Hello"} http://localhost:15320/process-prompt
