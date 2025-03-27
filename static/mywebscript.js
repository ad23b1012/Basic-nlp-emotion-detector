async function processText() {
    let text = document.getElementById("inputText").value;
    let response = await fetch("/process", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: text })
    });

    let data = await response.json();
    document.getElementById("output").innerText = JSON.stringify(data, null, 2);
}
