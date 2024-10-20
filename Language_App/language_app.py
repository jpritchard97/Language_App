import random

# Word list with French, Spanish, Dutch, and German
words = {
    "french": [
        {"foreign": "le", "english": "the"},
        {"foreign": "de", "english": "of/from"},
        {"foreign": "que", "english": "that/which"},
        {"foreign": "et", "english": "and"},
        {"foreign": "à", "english": "to/at"},
        {"foreign": "dans", "english": "in/on"},
        {"foreign": "un", "english": "a/an"},
        {"foreign": "être", "english": "to be"},
        {"foreign": "se", "english": "oneself/itself"},
        {"foreign": "non", "english": "no/not"},
        {"foreign": "avoir", "english": "to have"},
        {"foreign": "pour", "english": "for"},
        {"foreign": "avec", "english": "with"},
        {"foreign": "son", "english": "his/her/its"},
        {"foreign": "comme", "english": "like/as"},
        {"foreign": "faire", "english": "to do"},
        {"foreign": "pouvoir", "english": "to be able to"},
        {"foreign": "aller", "english": "to go"},
        {"foreign": "lequel", "english": "which"},
        {"foreign": "tout", "english": "all/everything"},
    ],
    "spanish": [
        {"foreign": "el", "english": "the"},
        {"foreign": "de", "english": "of/from"},
        {"foreign": "que", "english": "that/which"},
        {"foreign": "y", "english": "and"},
        {"foreign": "a", "english": "to/at"},
        {"foreign": "en", "english": "in/on"},
        {"foreign": "un", "english": "a/an"},
        {"foreign": "ser", "english": "to be"},
        {"foreign": "se", "english": "oneself/itself"},
        {"foreign": "no", "english": "no/not"},
        {"foreign": "haber", "english": "to have"},
        {"foreign": "por", "english": "for/by"},
        {"foreign": "con", "english": "with"},
        {"foreign": "su", "english": "his/her/your/their"},
        {"foreign": "para", "english": "for/to"},
        {"foreign": "como", "english": "like/as"},
        {"foreign": "estar", "english": "to be"},
        {"foreign": "tener", "english": "to have"},
        {"foreign": "todo", "english": "all/everything"},
        {"foreign": "algo", "english": "something"},
    ],
    "dutch": [
        {"foreign": "de", "english": "the"},
        {"foreign": "van", "english": "of/from"},
        {"foreign": "dat", "english": "that/which"},
        {"foreign": "en", "english": "and"},
        {"foreign": "naar", "english": "to/at"},
        {"foreign": "in", "english": "in/on"},
        {"foreign": "een", "english": "a/an"},
        {"foreign": "zijn", "english": "to be"},
        {"foreign": "zich", "english": "oneself/itself"},
        {"foreign": "nee", "english": "no/not"},
        {"foreign": "hebben", "english": "to have"},
        {"foreign": "voor", "english": "for"},
        {"foreign": "met", "english": "with"},
        {"foreign": "zijn", "english": "his/her/its"},
        {"foreign": "als", "english": "like/as"},
        {"foreign": "doen", "english": "to do"},
        {"foreign": "kunnen", "english": "to be able to"},
        {"foreign": "gaan", "english": "to go"},
        {"foreign": "welk", "english": "which"},
        {"foreign": "alles", "english": "all/everything"},
    ],
    "german": [
        {"foreign": "der", "english": "the"},
        {"foreign": "von", "english": "of/from"},
        {"foreign": "dass", "english": "that/which"},
        {"foreign": "und", "english": "and"},
        {"foreign": "zu", "english": "to/at"},
        {"foreign": "in", "english": "in/on"},
        {"foreign": "ein", "english": "a/an"},
        {"foreign": "sein", "english": "to be"},
        {"foreign": "sich", "english": "oneself/itself"},
        {"foreign": "nein", "english": "no/not"},
        {"foreign": "haben", "english": "to have"},
        {"foreign": "für", "english": "for"},
        {"foreign": "mit", "english": "with"},
        {"foreign": "sein", "english": "his/her/its"},
        {"foreign": "wie", "english": "like/as"},
        {"foreign": "tun", "english": "to do"},
        {"foreign": "können", "english": "to be able to"},
        {"foreign": "gehen", "english": "to go"},
        {"foreign": "welches", "english": "which"},
        {"foreign": "alles", "english": "all/everything"},
    ]
}

def quiz_user(language, words):
    """Quiz the user with words from the selected language."""
    random.shuffle(words)  # Shuffle the list of words
    score = 0

    for word in words:
        print(f"What is the English translation of '{word['foreign']}' in {language}?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['english'].lower()

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{word['english']}'.\n")

    print(f"Quiz complete! Your score: {score}/{len(words)}")

def main():
    print("Welcome to the Multilingual Flashcards App!")
    print("Available languages: French, Spanish, Dutch, German")
    
    language = input("Please select a language: ").strip().lower()

    if language in words:
        print(f"Starting quiz for {language.capitalize()}...")
        input("Press Enter to start the quiz...")
        quiz_user(language, words[language])
    else:
        print("Sorry, the selected language is not available.")

if __name__ == "__main__":
    main()
