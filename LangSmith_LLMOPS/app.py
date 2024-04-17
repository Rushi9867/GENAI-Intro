from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user request only based on the given context"),
        ("user","Question:{question}\nContext:{context}")
    ]
)

model = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()

chain = prompt|model|output_parser

question = "Can you summarize the Speech?"
context = """
Speech is a human vocal communication using language. Each language uses phonetic combinations of vowel and consonant sounds that form the sound of its words (that is, all English words sound different from all French words, even if they are the same word, e.g., "role" or "hotel"), and using those words in their semantic character as words in the lexicon of a language according to the syntactic constraints that govern lexical words' function in a sentence. In speaking, speakers perform many different intentional speech acts, e.g., informing, declaring, asking, persuading, directing, and can use enunciation, intonation, degrees of loudness, tempo, and other non-representational or paralinguistic aspects of vocalization to convey meaning. In their speech, speakers also unintentionally communicate many aspects of their social position such as sex, age, place of origin (through accent), physical states (alertness and sleepiness, vigor or weakness, health or illness), psychological states (emotions or moods), physico-psychological states (sobriety or drunkenness, normal consciousness and trance states), education or experience, and the like.

Although people ordinarily use speech in dealing with other persons (or animals), when people swear they do not always mean to communicate anything to anyone, and sometimes in expressing urgent emotions or desires they use speech as a quasi-magical cause, as when they encourage a player in a game to do or warn them not to do something. There are also many situations in which people engage in solitary speech. People talk to themselves sometimes in acts that are a development of what some psychologists (e.g., Lev Vygotsky) have maintained is the use of silent speech in an interior monologue to vivify and organize cognition, sometimes in the momentary adoption of a dual persona as self addressing self as though addressing another person. Solo speech can be used to memorize or to test one's memorization of things, and in prayer or in meditation (e.g., the use of a mantra).

Researchers study many different aspects of speech: speech production and speech perception of the sounds used in a language, speech repetition, speech errors, the ability to map heard spoken words onto the vocalizations needed to recreate them, which plays a key role in children's enlargement of their vocabulary, and what different areas of the human brain, such as Broca's area and Wernicke's area, underlie speech. Speech is the subject of study for linguistics, cognitive science, communication studies, psychology, computer science, speech pathology, otolaryngology, and acoustics. Speech compares with written language,[1] which may differ in its vocabulary, syntax, and phonetics from the spoken language, a situation called diglossia.

The evolutionary origins of speech are unknown and subject to much debate and speculation. While animals also communicate using vocalizations, and trained apes such as Washoe and Kanzi can use simple sign language, no animals' vocalizations are articulated phonemically and syntactically, and do not constitute speech.
"""

print(chain.invoke({"question":question,"context":context}))