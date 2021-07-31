document.getElementById('submit').onclick = function () {
  let brand_select = document.getElementById("brand");
  let brand = brand_select.options[brand_select.selectedIndex].value;

  let model = document.getElementById("model").value;

  let year = parseInt(document.getElementById("year").value);

  let range = parseInt(document.getElementById("range").value);

  let category_select = document.getElementById("category");
  let category = category_select.options[category_select.selectedIndex].value;

  let energy_select = document.getElementById("energy");
  let energy = energy_select.options[energy_select.selectedIndex].value;

  let volume = parseFloat(document.getElementById("volume").value);

  let horses = parseInt(document.getElementById("horses").value);

  let transmission_select = document.getElementById("transmission");
  let transmission = transmission_select.options[transmission_select.selectedIndex].value;

  let color_select = document.getElementById("color");
  let color = color_select.options[color_select.selectedIndex].value;

  let options_inputs = document.querySelectorAll("#options input[type='checkbox']");
  let options = {}
  for (let input of options_inputs) {
    options[input.value] = input.checked ? 1 : 0;
  }

  let papers_select = document.getElementById("papers");
  let papers = papers_select.options[papers_select.selectedIndex].value;

  let wilaya_select = document.getElementById("wilaya");
  let wilaya = wilaya_select.options[wilaya_select.selectedIndex].value;

  let town = document.getElementById("town").value;

  let offer_select = document.getElementById("offer");
  let offer = offer_select.options[offer_select.selectedIndex].value;

  features = {
    "brand": brand,
    "model": model,
    "year": year,
    "range": range,
    "category": category,
    "energy": energy,
    "volume": volume,
    "horses": horses,
    "transmission": transmission,
    "color": color,
    "papers": papers,
    "wilaya": wilaya,
    "town": town,
    "offer": offer
  }
  Object.assign(features, options);

  async function postData(url = '', data = {}) {
    const response = await fetch(url, {
      method: 'POST',
      mode: 'cors', 
      cache: 'no-cache',
      credentials: 'same-origin',
      headers: {
        'Content-Type': 'application/json'
      },
      redirect: 'follow',
      referrerPolicy: 'no-referrer',
      body: JSON.stringify(data)
    });
    return response.json();
  }

  postData('http://127.0.0.1:5000', features)
  .then(data => {
    if (data['price'] === undefined) {
      document.getElementById("message").textContent = data["error"]
    } else {
      document.getElementById("message").textContent = parseInt(data['price']) + " DZA"
    }
    // alert(JSON.stringify(data))
  });

  return false;
};