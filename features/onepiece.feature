Feature: AnimeFLV
@onepiece
 Scenario: el último episodio es el 999
   Given chrome rising
   When the user gets animeflv page
   And the user clicks one peace link
   Then the last episode is the 999th