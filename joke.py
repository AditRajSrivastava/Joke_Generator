import requests
import json
from datetime import datetime, timezone
import os
import logging
import sys
import time
import random
from colorama import init, Fore, Back, Style
import pyfiglet
import textwrap
from tqdm import tqdm

# Initialize colorama for cross-platform colored output
init(autoreset=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

class JokeGeneratorUI:
    def __init__(self):
        self.width = 80  # Increased width for better display
        self.joke_generator = JokeGenerator()

    def clear_screen(self):
        """Clear the console screen"""
        os.system('clear')  # Using clear for Linux

    def show_loading_animation(self):
        """Show a loading animation"""
        with tqdm(total=100, 
                 desc="Loading joke", 
                 bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.GREEN, Fore.RESET)) as pbar:
            for _ in range(10):
                time.sleep(0.1)
                pbar.update(10)

    def print_centered(self, text, color=Fore.WHITE):
        """Print text centered with color"""
        print(color + text.center(self.width) + Style.RESET_ALL)

    def print_box(self, text, color=Fore.WHITE):
        """Print text in a decorative box"""
        lines = textwrap.wrap(text, width=self.width - 4)
        print(color + "┌" + "─" * (self.width - 2) + "┐")
        for line in lines:
            print(color + "│" + line.center(self.width - 2) + "│")
        print(color + "└" + "─" * (self.width - 2) + "┘" + Style.RESET_ALL)

    def display_menu(self):
        """Display the main menu with styling"""
        self.clear_screen()
        # Create ASCII art title
        title_text = "Joke Generator"
        try:
            title = pyfiglet.figlet_format(title_text, font="slant")
        except Exception:
            # Fallback if font not available
            title = f"\n{title_text}\n"
        
        print(Fore.CYAN + title + Style.RESET_ALL)
        
        # Print session info
        current_time = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
        self.print_box(
            f"Date: {current_time}\n"
            f"User: {os.getenv('USER', 'Unknown')}",
            Fore.YELLOW
        )

        # Print menu options
        print(Fore.GREEN + "\n📜 Choose your joke category:" + Style.RESET_ALL)
        menu_items = [
            ("1", "Random Joke", "😄"),
            ("2", "Dad Joke", "👨"),
            ("3", "Chuck Norris Joke", "💪"),
            ("4", "Hindi Joke (हिंदी जोक)", "🇮🇳"),
            ("5", "Indian English Joke", "🎭"),
            ("6", "Exit", "👋")
        ]

        for num, item, emoji in menu_items:
            print(f"{Fore.CYAN}{emoji} [{num}] {Fore.WHITE}{item}")

    def display_joke(self, joke_text, category):
        """Display a joke with styling"""
        self.clear_screen()
        
        # Show category header
        header = f"=== {category} ==="
        self.print_centered(header, Fore.YELLOW)
        print()

        # Show loading animation
        self.show_loading_animation()
        print()

        # Display the joke in a box
        self.print_box(joke_text, Fore.GREEN)
        
        # Wait for user input
        input(Fore.CYAN + "\nPress Enter to continue..." + Style.RESET_ALL)

class JokeGenerator:
    def __init__(self):
        self.apis = {
            "official": "https://official-joke-api.appspot.com/random_joke",
            "dad": "https://icanhazdadjoke.com/",
            "chuck": "https://api.chucknorris.io/jokes/random"
        }
        self.current_user = os.getenv('USER', 'Unknown')

    def get_official_joke(self):
        try:
            response = requests.get(self.apis["official"])
            if response.status_code == 200:
                joke_data = response.json()
                return f"{joke_data['setup']}\n=> {joke_data['punchline']}"
            return "Failed to fetch joke"
        except Exception as e:
            logger.error(f"Error: {e}")
            return "Error fetching joke"

    def get_dad_joke(self):
        try:
            headers = {'Accept': 'application/json'}
            response = requests.get(self.apis["dad"], headers=headers)
            if response.status_code == 200:
                return response.json()['joke']
            return "Failed to fetch joke"
        except Exception as e:
            logger.error(f"Error: {e}")
            return "Error fetching joke"

    def get_chuck_norris_joke(self):
        try:
            response = requests.get(self.apis["chuck"])
            if response.status_code == 200:
                return response.json()['value']
            return "Failed to fetch joke"
        except Exception as e:
            logger.error(f"Error: {e}")
            return "Error fetching joke"

    def get_hindi_joke(self):
        jokes = [
            "संता: डॉक्टर साहब, मैं सो नहीं पाता।\n=> डॉक्टर: कब से?\nसंता: जब से आपने मेरी दवा का बिल भेजा है!",
            "टीचर: बताओ दुनिया का सबसे तेज जानवर कौन सा है?\n=> छात्र: चीता मैडम!\nटीचर: वेरी गुड! पर ये बताओ तुम्हें कैसे पता?\nछात्र: मैडम वो क्या है न, मेरी बीवी रोज कहती है... घर में चीता लगा के रखा है!",
        ]
        return random.choice(jokes)

    def get_indian_english_joke(self):
        jokes = [
            "Why did the Indian IT guy get fired?\n=> Because he took 'work from home' too literally and started coding from Nepal!",
            "What do you call an Indian who loves telling jokes?\n=> A Pun-dit!",
        ]
        return random.choice(jokes)

    def run_with_ui(self):
        """Run the joke generator with enhanced UI"""
        ui = JokeGeneratorUI()
        
        while True:
            ui.display_menu()
            choice = input(f"\n{Fore.YELLOW}Enter your choice (1-6): {Style.RESET_ALL}").strip()

            if choice == '6':
                ui.clear_screen()
                farewell = pyfiglet.figlet_format("Goodbye!", font="slant")
                print(Fore.CYAN + farewell + Style.RESET_ALL)
                ui.print_box("Thanks for using Joke Generator!", Fore.YELLOW)
                break

            joke_text = None
            category = None

            if choice == '1':
                joke_text = self.get_official_joke()
                category = "Random Joke"
            elif choice == '2':
                joke_text = self.get_dad_joke()
                category = "Dad Joke"
            elif choice == '3':
                joke_text = self.get_chuck_norris_joke()
                category = "Chuck Norris Joke"
            elif choice == '4':
                joke_text = self.get_hindi_joke()
                category = "Hindi Joke"
            elif choice == '5':
                joke_text = self.get_indian_english_joke()
                category = "Indian English Joke"
            else:
                print(f"{Fore.RED}\n❌ Invalid choice! Please enter a number between 1 and 6.{Style.RESET_ALL}")
                time.sleep(1)
                continue

            if joke_text:
                ui.display_joke(joke_text, category)

def main():
    try:
        joke_generator = JokeGenerator()
        joke_generator.run_with_ui()
    except KeyboardInterrupt:
        print("\nGoodbye!")
    except Exception as e:
        logger.error(f"Application error: {e}")
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")
        sys.exit(1)

if __name__ == "__main__":
    main()
