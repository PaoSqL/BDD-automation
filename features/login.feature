Feature: Login capability

    @smoke
    Scenario: I login with valid credentials
        Given home: I am a user on home page
        When home: I click bookstore application card
        When books: I click login button
        When login: I login with valid credential
        Then books: I should land on books page