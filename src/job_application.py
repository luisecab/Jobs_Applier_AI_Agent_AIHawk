from dataclasses import dataclass
from typing import Dict
from .job import Job

@dataclass
class JobApplication:
    job: Job
    application: Dict
    resume_path: str = ""
    cover_letter_path: str = ""
