## Inspiration
When looking for a parking spot, we don't only want the closest. Search engines like Google only provide the nearest parking spot available; we decided to create our algorithm to determine the "perfect" parking lot for the user's current location. We developed a process that takes many aspects of a parking lot such as the capacity, distance, and price to show you the best parking spot near a location.

## What it does
A user will visit the website on any browser, supported on mobile and desktop. It's a very simple website used to simplify the process, allowing a user to enter the address. The site will try to make suggestions based on previous successful searches. Upon a user entering their location, the website will go through its collection of data and finding the best spot for them. Resulting in a page with a map and cards of data shown to provide information about the parking spots and the recommended ones in order. A user can then take a look and decide whether they can make it to any of the options, and make their way to park!

## How I built it
The website has two parts to it. It has a front-end which is built on top of HTML/CSS and JavaScript. All of this is hosted with Apache which provides users access to the website. The second part of the site is run on Python; it's a separate web server that runs on port 8000. This is used to communicate information between the algorithmic part of our code with the designed front-end that the user sees. The two parts work seamlessly to provide the best experience to a user.

## Challenges I ran into
We initially tried to make the website to use TTC scheduling information, but the data we found for it was unreliable. The times were inaccurate and too complicated to piece together. So we found out about a dataset for parking spots. We had some trouble with JSON parsing and saving objects to a cookie, but once all those issues were ironed out we managed to have a complete website that works flawlessly!

## Accomplishments that I'm proud of
The design of the website we put a lot of time in perfecting the spacing and design putting as much thought into every detail to ensure the site was an attractive and enjoyable experience for the user. We also decided to make it as bare bones as possible for developers to make their changes to it! Using the Google Maps Javascript API to finally work has to be another awe-inspiring accomplishments due to how many times we fell into issues with it, but we finally did it!

## What I learned
Making such a simple design requires a lot of work and thought into detail. We spent 80% of our time on sorting out useful datasets. What we also learned is the knowledge of using longitude and latitude to calculate the distance between two locations. Furthermore, being able to make an algorithm which would compute the best option for the user to pick, we had to weight each factor carefully. This involved us thinking outside the box to places that we would have never considered traditionally.

## What's next for Parking Buddy
Parking Buddy has a long way to go. If we had more time, we would have spent some time incorporating peek hour system that will allow users to check whether a parking site is at its full capacity or not. By adjusting the algorithm,  users will receive a dynamic list based on the time intervals in order to provide a better experience for the clients. (During peak hours, maximum capacity will be weighted more than distance and prices.)

