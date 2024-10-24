import os
from dotenv import load_dotenv
from src.scraping.linkedin_scraper import scrape_linkedin_profiles
from src.email.generate_email import generate_personalized_email
from src.email.send_email import send_email
from src.utils.logger import log_message

# Load environment variables from .env
load_dotenv()


def main():
    # Step 1: Scrape LinkedIn Profiles
    log_message("Starting LinkedIn profile scraping...")

    try:
        recruiter_data = scrape_linkedin_profiles()
        if not recruiter_data:
            log_message("No recruiter data found. Exiting the process.")
            return
    except Exception as e:
        log_message(f"Error during scraping: {e}")
        return

    # log_message(f"Successfully scraped {len(recruiter_data)} profiles.")

    # # Step 2: Generate Personalized Emails
    # log_message("Generating personalized emails for each recruiter...")

    # for recruiter in recruiter_data:
        recruiter_name = recruiter.get("name")
        company_name = recruiter.get("company")
        job_title = recruiter.get("job_title")
        email_address = recruiter.get("email")
        # Replace with dynamic skills based on the job
        skills = "Python, Machine Learning, DevOps"
        # Customize this
        achievements = "Built a machine learning pipeline that reduced processing time by 30%."

        log_message(
            f"Generating email for {recruiter_name} at {company_name}...")

        try:
            email_content = generate_personalized_email(
                recruiter_name, company_name, job_title, skills, achievements)
            if not email_content:
                log_message(
                    f"Failed to generate email for {recruiter_name}. Skipping...")
                continue
        except Exception as e:
            log_message(f"Error generating email for {recruiter_name}: {e}")
            continue

        # Step 3: Send the Email
        log_message(f"Sending email to {recruiter_name} ({email_address})...")

        try:
            send_email(to_email=email_address,
                       subject=f"Application for {job_title} at {company_name}", body=email_content)
            log_message(f"Email sent to {recruiter_name} ({email_address}).")
        except Exception as e:
            log_message(f"Error sending email to {recruiter_name}: {e}")

    log_message("Process completed.")


if __name__ == "__main__":
    main()
