import os
import openai
from datetime import datetime
import random

openai.api_key = os.getenv("OPENAI_API_KEY")

topics = [
    "Best motorcycle helmets under $200",
    "Affordable motorcycle upgrades for beginners",
    "How to clean and maintain your bike chain",
    "Best travel accessories for solo travelers",
    "Top camping gear under $50",
    "Security guard must-have gear list",
    "Budget home security upgrades anyone can do",
]

def make_article(topic):
    prompt = f"""
    Write a 1200-word SEO-optimized article about: {topic}.
    Include:
    - engaging intro
    - 5 sections with headers
    - 3 product recommendations
    - list of pros/cons for each product
    - conclusion
    Do NOT mention AI. Format in markdown.
    """

    response = openai.chat.completions.create(
        model="gpt-5.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8
    )

    return response.choices[0].message["content"]

topic = random.choice(topics)
article = make_article(topic)

today = datetime.now().strftime("%Y-%m-%d")
filename = f"articles/{today}-{topic.replace(' ', '-')}.md"

os.makedirs("articles", exist_ok=True)
with open(filename, "w") as f:
    f.write(article)

print(f"Generated article: {filename}")
