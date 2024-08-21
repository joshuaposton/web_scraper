# Automated Web Scraper

This project is a Python-based web scraper that automatically scrapes article titles and links from TechCrunch, stores the data in an SQLite database, and can be run on a schedule. The scraper is designed to be flexible and can be easily adapted to other websites.

## Features

- **Automated Scraping**: The scraper runs at a specified time (e.g., daily) using Python’s `schedule` library.
- **Data Storage**: Scraped data is stored in an SQLite database, ensuring structured and scalable storage.
- **Duplicate Handling**: Duplicate articles are automatically ignored during the scraping process.

## Installation

### Prerequisites

- Python 3.x
- `requests`, `beautifulsoup4`, `pandas`, `sqlite3`, and `schedule` libraries (installed automatically via `requirements.txt`).

### Setting Up

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
