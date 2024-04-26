import os,requests,csv
from bs4 import BeautifulSoup
def scrape_and_save_to_csv(url, csv_filename):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        h2_tags = soup.find_all('h2')
        h3_tags = soup.find_all('h3')
        pre_tags = soup.find_all('pre')
        if not h2_tags and not h3_tags and not pre_tags:
            print(f"No relevant content found on {url}. Skipping CSV creation.")
            return
        if not os.path.exists('results'):
            os.makedirs('results')
        csv_path = os.path.join('results', csv_filename)       
        with open(csv_path, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Headings', 'Sub-Headings', 'Code'])
            if not h2_tags:
                if not h3_tags:
                    if pre_tags:
                        for pre_tag in pre_tags:
                            code_lines = [line.strip() for line in pre_tag.text.split('\n') if line.strip()]
                            writer.writerow(['', '', ' '.join(code_lines)])
                        print(f"Scraping and CSV creation successful for {url}.")
                        return
            if not h2_tags:
                for h3_tag in h3_tags:
                    sub_heading = h3_tag.text.strip().replace('#', '') 
                    code_snippet_element = h3_tag.find_next('div', class_='highlight-bash')
                    if code_snippet_element:
                        code_lines = [line.strip().replace('#', '') for line in code_snippet_element.text.split('\n') if line.strip() if line.strip()]
                        if len(code_lines) == 1:
                            writer.writerow(['', sub_heading, code_lines[0]])
                        else:
                            writer.writerow(['', sub_heading, ' '.join(code_lines)])
            else:
                for h2_tag in h2_tags:
                    current_heading = h2_tag.text.strip().replace('#', '')
                    sub_heading = ''
                    for h3_tag in h2_tag.find_all_next('h3'):
                        sub_heading = h3_tag.text.strip().replace('#', '')    
                        code_snippet_element = h3_tag.find_next('div', class_='highlight-bash')
                        if code_snippet_element:
                            code_lines = [line.strip().replace('#', '') for line in code_snippet_element.text.split('\n') if line.strip()]
                            if len(code_lines) == 1:
                                writer.writerow([current_heading, sub_heading, code_lines[0]])
                            else:
                                writer.writerow([current_heading, sub_heading, ' '.join(code_lines)])
                    if not h2_tag.find_all_next('h3'):    
                        code_snippet_element = h2_tag.find_next('div', class_='highlight-bash')
                        if code_snippet_element:
                            code_lines = [line.strip().replace('#', '') for line in code_snippet_element.text.split('\n') if line.strip()]
                            if len(code_lines) == 1:
                                writer.writerow([current_heading, sub_heading, code_lines[0]])
                            else:
                                writer.writerow([current_heading, sub_heading, ' '.join(code_lines)])
                        else:
                            code_snippet_element = h2_tag.find_next(class_='headerlink')
                            if code_snippet_element:
                                code_lines = [line.strip().replace('#', '') for line in code_snippet_element.text.split('\n') if line.strip()]
                            if len(code_lines) == 1:
                                writer.writerow([current_heading, sub_heading, code_lines[0]])
                            else:
                                writer.writerow([current_heading, sub_heading, ' '.join(code_lines)])
                            if not h2_tags:
                                print(f"No relevant content found on {url}. Skipping CSV creation.")
                                return
            print(f"Scraping and CSV creation successful for {url}.")
    else:
        print(f"Failed to retrieve page: {url}.")
urls_to_scrape = [
    "https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/",
    "https://packaging.python.org/en/latest/guides/installing-using-virtualenv/",
    "https://packaging.python.org/en/latest/guides/installing-stand-alone-command-line-tools/",
    "https://packaging.python.org/en/latest/guides/installing-using-linux-tools/",
    "https://packaging.python.org/en/latest/guides/installing-scientific-packages/"
]
for index, url in enumerate(urls_to_scrape, start=1):
    csv_filename = f'installationguide_step{index}.csv'
    scrape_and_save_to_csv(url, csv_filename)
