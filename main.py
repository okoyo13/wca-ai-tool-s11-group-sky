from openai import OpenAI
from dotenv import load_dotenv
import os
import json

# Load API key from .env
load_dotenv()

client = OpenAI(api_key=os.getenv("OpenAI_API_KEY"))



# KNOWLEDGE BASE

KNOWLEDGE_BASE = """
IYF We Can Academy student knowledge base

ARTIFICIAL INTELLIGENCE (AI):

Artificial Intelligence (AI) is anything that mimics human
intelligence by automating human tasks.


SCHOOL PROGRAM INFORMATION:

1. Classes run only on Saturdays and Sundays.

2. We have two classes per day for this course:
   - 10:00 AM to 12:00 PM
   - 2:00 PM to 4:00 PM

3. Class duration is 2 hours per session.

4. The classroom is found in the MIS building,
   second floor, room 205.

5. The teacher's name is Mr. Daniel Chacha,
   but you can call him Chacha. He is a very friendly
   and approachable teacher.

6. You can reach him through:
   Email: daniel.chacha@we-can-academy.org
   Cell: +254 796 280 700

7. Chapel classes are held on Saturdays ONLY
    -08:00 AM to 10:00 AM.
    -12:00 PM to 2:00 PM.


8. The chapel is located on the first floor,
   conference room. It is mandatory for students
   and is part of the curriculum.

9. For this course, students should have:
   - A book
   - A pen
   - A laptop

10. Chapel class duration is 2 hours per session.

11. Each student must attend four chaplain consultation
    sessions during the three-month program. Attendance
    will be recorded by scanning the passport.

12. For enrollment, a registration/commitment fee of
    KES 1,000 is required, which includes a class passport booklet.

13. A graduation fee will be payable by all students
    who successfully complete the program.

14. We only accept cash payment. A receipt will be given
    as proof of payment. Every receipt should be kept safe
    until graduation.

15. Three absences will result in expulsion.

16. Missed classes can be recovered by meeting your chaplain.

17. Any attempt to scan another student's QR code to record
    false attendance is considered fraud and will result
    in immediate expulsion.

18. You need to scan your passport:
    - At the entrance
    - After every class
    - After Chapel class sessions
    - After Chaplain consultation

19. A link will be provided to you by your class teacher
    that will help you track your attendance.

20. You need to know at least one programming language,
    have a good laptop for this course, and have a positive
    mind that is ready to learn.

21. The Head Chaplain is known as Mika.
    Contact: +254 768 653 081

22. Mr. Kennedy is in charge of the chapel class.

23. The course takes 3 months to complete.
"""



# SAVE OUTPUT


def save_output(result):
    """Save the latest AI response to output.txt."""

    try:
        with open("output.txt", "w", encoding="utf-8") as file:
            file.write(result)

        print("\nOutput saved successfully to output.txt")

    except Exception as error:
        print("\nCould not save output.")
        print(error)



# MAIN CHATBOT


def main():
    """Start the IYF Expounder with conversation memory."""

    print("==========================================")
    print("       IYF EXPOUNDER STUDENT SUPPORT BOT")
    print("==========================================")

    print("\nWelcome to AI!")

    print("Ask me any question about the AI.") 

    print("Type 'exit' to end the conversation.\n")

    # Stores previous questions and answers
    conversation_history = []

    while True:

        student_question = input("Student: ").strip()

        # Exit chatbot
        if student_question.lower() == "exit":
            print("\nThank you for using IYF Expounder!")
            print("GoodLuck!")
            break

        # Empty question
        if not student_question:
            print("\nPlease enter a question.\n")
            continue

 
        # RTCCO PROMPT
     

        prompt = f"""
ROLE:
You are the IYF We Can Academy Student Support Bot.

TASK:
Answer the student's current question using ONLY the
information contained in the knowledge base.

CONTEXT:

KNOWLEDGE BASE:
{KNOWLEDGE_BASE}

PREVIOUS CONVERSATION:
{conversation_history}

CURRENT STUDENT QUESTION:
{student_question}

CONSTRAINTS:
- Use ONLY information contained in the knowledge base.
- Do NOT use outside knowledge.
- Do NOT invent information.
- Do NOT make assumptions.
- Do NOT create examples unless they are explicitly
  contained in the knowledge base.
- Do NOT add information that is not contained in the
  knowledge base.
- Use the previous conversation only to understand
  follow-up questions.
- If the requested information is not contained in the
  knowledge base, clearly state that the information
  is not available and human intervention is required.
- If the question is unclear or ambiguous, ask the
  student to clarify.
- Do not invent school policies, fees, schedules,
  contacts, locations, or attendance rules.
- Use simple English.
- Be polite and helpful.

OUTPUT:
- Answer the student's current question.
- Use previous conversation when necessary.
- Give a clear and concise answer.
- Do not include unrelated information.
"""

        try:

            print("\nBot is thinking...")

            # OpenAI Responses API
            response = client.responses.create(
                model="gpt-5.4-mini",
                input=prompt
            )

            # Get the AI response
            result = response.output_text

            # Display response
            print("\n===== BOT =====")
            print(result)

            # Save conversation
            conversation_history.append({
                "role": "user",
                "content": student_question
            })

            conversation_history.append({
                "role": "assistant",
                "content": result
            })

            # Save latest answer to output.txt
            save_output(result)

            print()

        except Exception as error:

            print("\n===== ERROR =====")
            print("The bot could not generate a response.")
            print(error)
            print()


# START PROGRAM

if __name__ == "__main__":
    main()