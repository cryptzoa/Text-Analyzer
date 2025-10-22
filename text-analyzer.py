import sys
from collections import Counter
import re
import matplotlib.pyplot as plt

def analyze(filename):
    with open(filename, encoding='utf-8') as f:
        text = f.read().lower()

    words = re.findall(r"\b[a-z0-9']+\b", text)
    total_words = len(words)
    avg_len = sum(len(w) for w in words) / total_words if total_words else 0
    freq = Counter(words)

    # === Fitur Hitung Jumlah Kalimat, Paragraf, Karakter ===
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    paragraphs = [p for p in text.split('\n') if p.strip()]
    characters = len(text)

    # Output ke terminal
    print("Total words:", total_words)
    print("Total sentences:", len(sentences))
    print("Total paragraphs:", len(paragraphs))
    print("Total characters:", characters)
    print("Average word length: {:.2f}".format(avg_len))
    print("Top 10 words:", freq.most_common(10))

    # === Ekspor hasil ke file ===
    with open("output.txt", "w", encoding="utf-8") as out:
        out.write(f"Total words: {total_words}\n")
        out.write(f"Total sentences: {len(sentences)}\n")
        out.write(f"Total paragraphs: {len(paragraphs)}\n")
        out.write(f"Total characters: {characters}\n")
        out.write(f"Average word length: {avg_len:.2f}\n\n")
        out.write("Top 10 words:\n")
        for word, count in freq.most_common(10):
            out.write(f"{word}: {count}\n")

    # === Grafik frekuensi kata ===
    top_words = freq.most_common(10)
    words_list, counts = zip(*top_words)
    plt.bar(words_list, counts)
    plt.title("Top 10 Most Frequent Words")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 analyzer_plus1.py file.txt")
    else:
        analyze(sys.argv[1])
