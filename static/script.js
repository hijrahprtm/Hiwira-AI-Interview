const btn = document.getElementById("talkBtn");
const chatbox = document.getElementById("chatbox");

const recognition = new(window.SpeechRecognition || window.webkitSpeechRecognition)();

recognition.lang = "id-ID";

btn.onclick = () => {
    recognition.start();
};

recognition.onresult = async (event) => {

    const userText = event.results[0][0].transcript;

    chatbox.innerHTML += `<p><b>Lo:</b> ${userText}</p>`;

    const response = await fetch("/chat", {
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            message:userText
        })
    });

    const data = await response.json();

    chatbox.innerHTML += `<p><b>AI HR:</b> ${data.response}</p>`;

    const speech = new SpeechSynthesisUtterance(data.response);

    speech.lang = "id-ID";

    window.speechSynthesis.speak(speech);
};