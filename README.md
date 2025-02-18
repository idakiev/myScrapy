# myScrapy

A small project focused on retrieving information from a web store.

---
## Installation

1. Clone the repository:
    ```
      https://github.com/idakiev/myScrapy.git
    ```
3. Install dependencies:
    ```
      pip install -r requirements.txt
    ```
4. Navigate to scrapy project folder.
    ```
      cd myScrapy/mini_scrapy
    ```
5. Run 'scrape.py':
    ```
      python scrape.py
    ```
6. Find the scraped data in 'filtered_data.json':
   ```
   {
    "name": String,
    "colour": String,
    "availableColours": List,
    "reviews_count": Int,
    "reviews_score": Float,
   }
   ```

## License
This section is licensed under the [MIT License](LICENSE).
