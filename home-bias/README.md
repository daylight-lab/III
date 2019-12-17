# home-bias

This notebook calculates "home bias" in website visits using Alexa rankings.

We first scrape the list of most popular websites in the world. We then scrape the most popular websites in each country. We compute home bias for a given country by computing the Levenshtein distance between a country's most popular websites and the global most popular websites.

# Repository

We scrape data in the `data-collection.ipynb` notebook. Output goes into the `data/` folder.

## Requirements
- Python3
- Jupyter

### Python packages:

- BeautifulSoup
- Requests
- Funcy
- textdistance

# TODO

1. I can't get site-specific info wtihout a paid account (so I can't tell what country sites are from)
2. From a "home bias" perspective, websites aren't really like equities. Linguistic, cultural, and local-specific sources make it impractical for people to visit websites from all over the world. All to say, our baseline assumption (in a fully interopable world, there will be no home bias in website visits) isn't necessarily great. That said... it may not matter. After all, there may be more or less home bias, differences in home bias may increase or decrease over the course of years, etc.
3. A better (and still-practical) metric might be to understand each website as a proportion of global traffic. In the home bias example, that's sort of like accounting for US equities as a proportion of global equities.
