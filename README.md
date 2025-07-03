
<div align="center">


# AIHawk: the first Jobs Applier AI Agent


AIHawk's core architecture remains **open source**, allowing developers to inspect and extend the codebase. However, due to copyright considerations, we have removed all third‑party provider plugins from this repository.

For a fully integrated experience, including managed provider connections: check out **[laboro.co](https://laboro.co/)** an AI-driven job board where the agent **automatically applies to jobs** for you.


---


AIHawk has been featured by major media outlets for revolutionizing how job seekers interact with the job market:

[**Business Insider**](https://www.businessinsider.com/aihawk-applies-jobs-for-you-linkedin-risks-inaccuracies-mistakes-2024-11)
[**TechCrunch**](https://techcrunch.com/2024/10/10/a-reporter-used-ai-to-apply-to-2843-jobs/)
[**Semafor**](https://www.semafor.com/article/09/12/2024/linkedins-have-nots-and-have-bots)
[**Dev.by**](https://devby.io/news/ya-razoslal-rezume-na-2843-vakansii-po-17-v-chas-kak-ii-boty-vytesnyaut-ludei-iz-protsessa-naima.amp)
[**Wired**](https://www.wired.it/article/aihawk-come-automatizzare-ricerca-lavoro/)
[**The Verge**](https://www.theverge.com/2024/10/10/24266898/ai-is-enabling-job-seekers-to-think-like-spammers)
[**Vanity Fair**](https://www.vanityfair.it/article/intelligenza-artificiale-candidature-di-lavoro)
[**404 Media**](https://www.404media.co/i-applied-to-2-843-roles-the-rise-of-ai-powered-job-application-bots/)

## Setup

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Place your configuration files in the `data_folder/` directory:
   - `secrets.yaml` containing your `llm_api_key`
   - `work_preferences.yaml`
   - `plain_text_resume.yaml`
   - `resume.pdf` *(optional)* if you want to reuse an existing resume
3. Run the application:
   ```bash
   python main.py
   ```
   Follow the prompts to generate resumes or cover letters. When `resume.pdf` is present, it will be copied instead of generating a new resume.

