import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_personalized_email(recruiter_name, company_name, job_title, your_skills, achievements):
    prompt = f"""
    Write a personalized email to {recruiter_name}, a recruiter at {company_name}, where I am applying for a {job_title} position. 
    Mention my skills in {your_skills} and highlight achievements such as {achievements}. The email should be professional, courteous, 
    and showcase why I would be a good fit for their team.
    """

    try:
        # Call OpenAI GPT-4 model to generate an email
        response = openai.Completion.create(
            # Use "gpt-4" if you have access to GPT-4, or adjust accordingly
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=300,
            n=1,
            stop=None,
            temperature=0.7,
        )

        # Extract the generated email
        email_content = response['choices'][0]['text'].strip()
        return email_content

    except Exception as e:
        print(f"Error generating email: {str(e)}")
        return None


# # Example usage
# if __name__ == "__main__":
#     recruiter_name = "John Doe"
#     company_name = "Tech Innovators"
#     job_title = "Software Engineer"
#     your_skills = "Python, Machine Learning, DevOps"
#     achievements = "building a machine learning pipeline that improved processing time by 30%"

#     email = generate_personalized_email(
#         recruiter_name, company_name, job_title, your_skills, achievements)

#     if email:
#         print("\nGenerated Email:\n")
#         print(email)
