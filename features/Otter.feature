Feature: As a consuemr I want to search some pets in google from an API

    Scenario Outline: I_search_in_browser_some_pets
        Given I get information from this API "<api_url>"
        When then I search each pet in "<search_engine>"
        Then I see the first result in the results page

        Examples:
            | api_url                    | search_engine |
            | http://localhost:3000/dogs | google        |