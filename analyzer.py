from skills import required_skills

print("===== AI Resume Analyzer =====")

resume = input("\nPaste your resume text:\n").lower()

found_skills = []
missing_skills = []

for skill in required_skills:
    if skill in resume:
        found_skills.append(skill)
    else:
        missing_skills.append(skill)

score = (len(found_skills) / len(required_skills)) * 100

print("\n===== ANALYSIS REPORT =====")

print("\nSkills Found:")
for skill in found_skills:
    print("✓", skill)

print("\nMissing Skills:")
for skill in missing_skills:
    print("✗", skill)

print(f"\nResume Score: {score:.2f}%")

if score >= 80:
    print("Excellent Resume!")
elif score >= 50:
    print("Good Resume. Add more skills.")
else:
    print("Needs Improvement.")