import requests
from bs4 import BeautifulSoup


def scrape_weather_data():
	response = requests.get("http://mfd.gov.np/weather/")

	soup = BeautifulSoup(response.text, "lxml")

	places_table = soup.select("body > div.tab-content > div.container.main-body > div > div:nth-child(1) > div")[0]
	places_table = places_table.find_all("table")[0]

	table_rows = places_table.find_all("tr")
	table_rows.remove(table_rows[0])
	table_rows.remove(table_rows[-1])


	extracted_data = []

	for row in table_rows:
		table_data = row.find_all("td")
		extracted_data_dict = dict()
		data_list = []
		for data in table_data:
			data_list.append(data.text)

		extracted_data_dict["place"] = data_list[0]
		extracted_data_dict["max_temp"] = data_list[1]
		extracted_data_dict["min_temp"] = data_list[2]
		extracted_data_dict["rainfall"] = data_list[3]

		extracted_data.append(extracted_data_dict)


	return extracted_data


print(scrape_weather_data())