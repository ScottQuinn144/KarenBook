# **KarenBook**
Welcome to Karenbook. This program is a basic social media site that allows users to voice unpopular opinions. 
Everyone has there own profile and ability to post, edit or delete their posts as well as comment on others. 
Following and unfollowing other profiles is allowed.

The live site to Battleships : [Click Here](https://karenbook.herokuapp.com/)

## **Aim**

#### User-
- The User wants to be able to sign in, post and comment on material throughout the site. Not only can they do this they can also follow and unfollow profiles as well.

#### Developer-
- The main aim for the developer is to create a bug free program which allows users to enjoy a simple social media site while also providing scope to improve and add more complexity and functionality to the program in later iterations.

- The second aim is for the developer to showcase his python and django skills within the coding of this program. Using the BDD method of testing, the developer's aim in the first release is to create a program without bugs.

## **Modals**
- I have created 3 models to store information. They are Profile, Posts and Comment. Each is self explained but are connect to allow users to have a profile, post to the site and comment as well.

- In the future I would look at making this program with a TDD approach however with limited timing a BDD approach was prefered.


## **Features**

### Sign In / Sign Up capability
- Using Django's built in User package, each user will have the ability to create there own account and 
from that information, be able to log in and log out whenever they choose. Once the user profile is created, the automatically follow thier own profile
 


### Posts
- Each user will have the ability to add a post that automatically is added to the newsfeed of anyone who follows them. They will also have the ability to edit and delete posts that they have created



### Comments
- Each signed in user will have the ability to create posts on any post within the website.




## **Future features**
 In future iterations, users will be able to search for user's via a search bar in profile_list.html and also be able to upload a profile picture. 


## **Bugs**
 I have manually tested the program

 - Data validation tested within GitPod's terminal
 - Data validation tested in the deployed site on Heroku
 - Passed the PEP8 online validator
 - Step by step running through Python Tutor
 
 Throughout the building of the program many small bugs came up. Those were:

 <ul>
    <li> Unable to connect comments to posts </li>
    <li> Unable to log in </li>
    <li> Changing models so that old data was corrupted and page would not load </li>
</ul>


## **Current Bugs**
- There are no current bugs from a users perspective in this program when I tested it using the BDD method. 


## **Testing**
Testing was completed by PEP8 online checker with no issues in python code.
<br>
I chose to go with BDD: behavior-driven development style of testing with this program. Results where positive

<ul>
    <li> Given the user visited the site, 
When the user clicked the signup button, 
Then ensure the user can access the signup page</li>
<br>
    <li> Given the user wrote a post on the site, 
When the user's followers go on thier Newsfeed the new post will appear,
Then the post has been successfully added</li>
<br>
    <li> Given the user has a profile, 
When the user clicks the profile button in the navbar,
Then then the user's profile will appear</li>
<br>
    <li> Given the user wrote a post on the site, 
When the user's clicks to edit the post,
Then an edit page is produced and fuctional</li>
<br>
    <li> Given the user wrote a post on the site, 
When the user clicks delete on a post,
Then the post has been successfully deleted</li>
<br>
    <li> Given the user has a profile on the site, 
When the user's clicks follow or unfollow on a profile,
Then the profile will unfollow or follow updating the site in the process</li>
<br>
    <li> Given the user has a profile, 
When the user's clicks logout,
Then the logout page opens and is functional</li>
</ul>

<br>

## **Design**
The design phase was created by the developer in his personal art studio. The colour schemes refect a softer tone to invite and welcome people to teh site. Clear and contrasting colours were chosen to maximize UI. Information is displayed as needed with no clutter to affect the UI. 

## **Deployment**

Site deployment guide:
<ol>
    <li>Log into Heroku Account</li>
    <li>Create new heroku app</li>
    <li>Add config vars</li>
    <li>Link github repository to heroku app via deploy tab/deployment method</li>
    <li>Enable Automatic deploy</li>
</ol>

- My deployed site url: ['https://karenbook.herokuapp.com/'](https://karenbook.herokuapp.com/)

## **Credit to Libriraries and Programs**
- Django
- Python
- Cloudinary ( for future iterations )
- AllAuth

## **Credits**
Code Institute
- Code Institute -This project is a projection of the learning material learnt on Code Institute's learning platfom.
- The template for this project
- Project idea 
- Tutor support for being helpful and understanding in the development phase of this projects
<br>

NTi Gymnasiet ( my workplace )
Slack Overflow
<br>
Django and built in packages

## **Disclaimer**

This site was built for educational purposes only. All rights to the title name, KarenBook idea or others remain with the copyright owners. `Karenbook` is an educational project by the developer.

Developer: Scott Quinn
