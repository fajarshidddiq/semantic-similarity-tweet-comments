### Project Overview:

**Project Name:** Tweet Scraper

**Description:**  
This project utilizes the `twscrape` library as the main tool for scraping Twitter data. The current functionality allows for the scraping of comments based on tweet ID. Future enhancements and features are planned.

---

### How to Run:

1. Create a new conda environment:

    ```bash
    conda create --name myenv python=3.11
    ```

2. Activate the newly created environment:

    ```bash
    conda activate myenv
    ```

3. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the authentication script:

    ```bash
    python auth.py
    ```

5. Finally, execute the tweet scraping script:
    ```bash
    python tweet_comments.py
    ```
