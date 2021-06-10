const getData = async () => {
	let response = await fetch("https://weather.aayam555.repl.co/api/weather_data");
	let json = response.json();
	return json;
}	

const showData = async () => {
	const table = document.getElementById("weather-data");
	const data = await getData();

	table_html = `
	<thead>
		<tr>
			<th>Place</th>
			<th>Maximum Temp (&degC)</th>
			<th>Minimum Temp (&degC)</th>
			<th>24 hrs Rainfall (mm)</th>
		</tr>
	</thead>
`;

	for (let data_index = 0; data_index < data.length; data_index++){
		table_html += `<tbody><tr>
			<td>${data[data_index].place}</td>
			<td>${data[data_index].max_temp}</td>
			<td>${data[data_index].min_temp}</td>
			<td>${data[data_index].rainfall}</td>
		</tr><tbody>`

	table.innerHTML = table_html
	}
}

	

showData();
