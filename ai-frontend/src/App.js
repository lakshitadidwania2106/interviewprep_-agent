import { useState } from "react";

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { role: "user", text: input };

    setMessages(prev => [...prev, userMessage]);

    const response = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: input }),
    });

    const data = await response.json();

    const botMessage = { role: "bot", text: data.response };

    setMessages(prev => [...prev, botMessage]);
    setInput("");
  };

  return (
    <div style={styles.container}>
      <h2>🤖 AI Agent</h2>

      <div style={styles.chatBox}>
        {messages.map((msg, index) => (
          <div
            key={index}
            style={
              msg.role === "user" ? styles.userMessage : styles.botMessage
            }
          >
            {msg.text}
          </div>
        ))}
      </div>

      <div style={styles.inputContainer}>
        <input
          style={styles.input}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type a message..."
        />
        <button style={styles.button} onClick={sendMessage}>
          Send
        </button>
      </div>
    </div>
  );
}

const styles = {
  container: {
    width: "400px",
    margin: "50px auto",
    fontFamily: "Arial",
  },
  chatBox: {
    height: "400px",
    border: "1px solid #ccc",
    padding: "10px",
    overflowY: "scroll",
    marginBottom: "10px",
  },
  userMessage: {
    textAlign: "right",
    margin: "5px",
    color: "blue",
  },
  botMessage: {
    textAlign: "left",
    margin: "5px",
    color: "green",
  },
  inputContainer: {
    display: "flex",
  },
  input: {
    flex: 1,
    padding: "10px",
  },
  button: {
    padding: "10px",
  },
};

export default App;