# basic-scraper

###This repository holds sample code for a scraping health inspection data from King County

*Feb 16th, 2015* - Added basic scraper

                      1. get_inspection_page(value): submits a search and gets data from webpage and writes it to a file
                      2. load_inspection_page(): loads inspection data html from file
                      3. parse_source(): pass inspection data html through BeautifulSoup
                      4. extract_data_listings(): returns all restaurant listings
                      5. has_two_tds(): filter restaurant listings to find the ones with two <td> elements
                      6. clean_data(): string extra characters from restuarant metadata
                      7. extract_restaurant_metadata(): returns the restaurant metadata
                      8. is_inspection_row(): find the rows of restaurant data that have inspection data
                      9. extract_score_data(): return inspection scores
