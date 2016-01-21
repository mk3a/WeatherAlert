# WeatherAlert
Texts me weather alerts if the weather is too bad.
###Usage
It uses uwaterloo's open data to extract weather info and hence works for only waterloo.
I chose uwaterloo's open data and not something more general as I live on campus and I think the data source I chose is more accurate for local uwaterloo weather than the general waterloo region weather.

A twilio account (free) is needed for the script to text you. You don't have to worry about entering the authentication tokens as the script will ask for what is missing and also allows you to change if you so desire by passing a second parameter as true to the message function.

To run the script automatically I use Launchd on Mac with gem lunchy.
Here is a nice tutorial on it. http://killtheyak.com/schedule-jobs-launchd/
