@PRC
Feature: Testing user login

  Background: common steps
    Given user is on login page
     When  User enters valid credentials
     And   Clicks login
     When user should navigate to PRC.News dashboard
     And Open Account dropdown

@tags1
  Scenario: User should navigate to the Manage Profile Screen
     Then Clicks on Manage Profile
     Then Clicks on Edit Profile
     Then Edit Fields
     And tap on save button


@tags2
  Scenario: User can edit their sign in method
     Then Clicks on Manage Profile
     And sign in method
     And enter new email
     Then clicks on cancel button

@tags3
   Scenario: User can edit their password
     Then Clicks on Manage Profile
     And click on reset password
     Then enter current password
     And enter new password
     And enter confirm password
     Then click on cancel password


