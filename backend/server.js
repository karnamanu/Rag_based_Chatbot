import express from "express";
import fetch from "node-fetch";

const app = express();
app.use(express.json());

app.post("/add", async (req, res) => {
  const response = await fetch("http://127.0.0.1:5000/add", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(req.body)
  });
  res.json(await response.json());
});

app.post("/chat", async (req, res) => {
  const { question } = req.body;

  const response = await fetch("http://127.0.0.1:5000/search", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query: question })
  });

  const data = await response.json();

  res.json({
    answer: "Based on Endee search:",
    context: data.contexts
  });
});

app.listen(3000, () => {
  console.log("Backend running on port 3000");
});
