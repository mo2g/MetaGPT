import os
import metagpt.utils.minecraft as utils
from metagpt.logs import logger


def load_skills_code(skill_names=None):
    skills_dir = os.path.dirname(os.path.abspath(__file__))
    if skill_names is None:
        skill_names = [
            skill[:-3] for skill in os.listdir(f"{skills_dir}") if skill.endswith(".js")
        ]
    skills = [
        utils.load_text(os.path.join(skills_dir, f"{skill_name}.js"))
        for skill_name in skill_names
    ]
    return skills