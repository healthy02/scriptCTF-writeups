# OSINT - The Insider

## Insider


    Someone from our support team has leaked some confidential information. Can you find out who?

Just looked up the Discord profiles of the moderators, and you find the flag in the Bio of the user `NoobMaster`.

![why this image not loadin](./attachments/discord1.png "this is too fucking easy haha" )


`scriptCTF{1ts_0bv10u5ly_j0hn_d03_aka_n00bm4573r}`

## Insider 2

    You found out the insider, but can you find what they leaked on GitHub and put it to use?

We started overthinking and kept going through GitHub like maniacs. We found the real names of the organizers, their YouTube channels and honestly it was kind of embarrasing to be bamboozled by a bunch of 15 year olds.


But in the end the solution was right under our noses. In the profile of the user `NoobMaster`, his GitHub profile `NoobMaster9999` was mentioned along with another link https://play.scriptsorcerers.xyz/users/340 

![why this image not loadin](./attachments/discord2.png "right under our noses" )

In one of the repositories, we were greeted by this. They leaked that there is going to be a scriptCTF 2026. Duh!

![why this image not loadin](./attachments/id_pass.png "creds are credentials fuuuuck" )

This is the Login ID and Password to be used when we go to the website and enter it, it gives us the flag.

`scriptCTF{scriptCTF_2026_leaked?!!}`

## Insider 3

    It's a tradition at this point. Continue where you left off...

We solved **Insider 3** and **Insider 4** before **Insider 2** lol. We were scouring through the GitHub of the same user when we came across this. We knew it was legit as it was commited by the same user `NoobMaster9999`

![why this image not loadin](./attachments/insider3_github.png "ez peazy" )

`scriptCTF{2026_fl4g_f0und_1n_2025}`


## Insider 4

    Good luck! Note: max flag limit is 6 for a reason, you should be able to get it in less than that. If not, open a ticket. Flag is case insensitive

2 Images and text file were attached in the same repository under the name of the `.insider-4`

![why this image not loadin](./attachments/rep.png "these are a lot of files" )

The `.secret` was 

    as a photographer, i add comments/descriptions to my images

So I used strings function on `fireworks.jpg` which revealed 

    Great fireworks! Thanks to the Wendell family for organizing these!

By simple Google search I found the town Rockport, TX, USA. 

By observing the view from the hotel room, we can see that the hotel is near a water body and and then there is some land and then some more water. Also in the background there is a pair of distinct buildings with a black roof. 

![why this image not loadin](./attachments/room.png "what kind of deadass photo is this" )

So I located this on the google earth, and then traversed the street view of the road and then found the building. 

![why this image not loadin](./attachments/google_earth.png "take me to the beach plss" )

`Days Inn by Wyndham`, after going through several images of the hotel on google maps I came across this image which labelled the room number as 214, and showed a red building in the background.

![why this image not loadin](./attachments/room_no.png "i created an alt for checking room numbers" )

So after a lot of brainstorming and arguments we used the 6 tries and finally hit jackpot on room no. 111.

`scriptCTF{901_Hwy_35_N_111}`


---
