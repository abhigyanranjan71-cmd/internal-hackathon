

mentors = []
mentees = []


def display_banner():
    print("\n" + "=" * 55)
    print("   🎓  PEER MENTORSHIP PLATFORM  🎓")
    print("   Connecting Students for Better Futures")
    print("=" * 55)


def display_menu():
    print("\n📋  MAIN MENU")
    print("-" * 35)
    print("  1. ➕  Add Mentor")
    print("  2. ➕  Add Mentee")
    print("  3. 🔍  Match Mentor for a Mentee")
    print("  4. ⭐  Give Feedback to a Mentor")
    print("  5. 📄  View All Mentors")
    print("  6. 🚪  Exit Program")
    print("-" * 35)


def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        print(f"  ⚠️  Please enter one of: {', '.join(valid_options)}")


def add_mentor():
    print("\n" + "─" * 40)
    print("  ➕  REGISTER AS A MENTOR")
    print("─" * 40)

    name    = input("  Enter your name          : ").strip()
    branch  = input("  Enter your branch        : ").strip().lower()
    year    = input("  Enter your current year  : ").strip()
    contact = input("  Enter your contact/email : ").strip()

    print("\n  Career Interest Areas (choose all that apply):")
    print("  [1] Software Development   [2] Data Science")
    print("  [3] Machine Learning       [4] Cybersecurity")
    print("  [5] Research               [6] Product Management")
    print("  [7] Other")

    raw    = input("  Enter numbers separated by commas (e.g. 1,3): ").strip()
    choices = [c.strip() for c in raw.split(",")]

    interest_map = {
        "1": "software development",
        "2": "data science",
        "3": "machine learning",
        "4": "cybersecurity",
        "5": "research",
        "6": "product management",
        "7": "other"
    }
    interests = [interest_map.get(c, "other") for c in choices if c in interest_map]

    if not interests:
        interests = ["general"]

    mentor = {
        "id"        : len(mentors) + 1,
        "name"      : name,
        "branch"    : branch,
        "year"      : year,
        "contact"   : contact,
        "interests" : interests,
        "ratings"   : [],
        "feedback"  : []
    }

    mentors.append(mentor)
    print(f"\n  ✅  Mentor '{name}' registered successfully! (ID: {mentor['id']})")


def add_mentee():
    print("\n" + "─" * 40)
    print("  ➕  REGISTER AS A MENTEE")
    print("─" * 40)

    name   = input("  Enter your name          : ").strip()
    branch = input("  Enter your branch        : ").strip().lower()
    year   = input("  Enter your current year  : ").strip()

    print("\n  Career Interest Areas (choose all that apply):")
    print("  [1] Software Development   [2] Data Science")
    print("  [3] Machine Learning       [4] Cybersecurity")
    print("  [5] Research               [6] Product Management")
    print("  [7] Other")

    raw     = input("  Enter numbers separated by commas (e.g. 2,4): ").strip()
    choices = [c.strip() for c in raw.split(",")]

    interest_map = {
        "1": "software development",
        "2": "data science",
        "3": "machine learning",
        "4": "cybersecurity",
        "5": "research",
        "6": "product management",
        "7": "other"
    }
    interests = [interest_map.get(c, "other") for c in choices if c in interest_map]

    if not interests:
        interests = ["general"]

    mentee = {
        "id"       : len(mentees) + 1,
        "name"     : name,
        "branch"   : branch,
        "year"     : year,
        "interests": interests
    }

    mentees.append(mentee)
    print(f"\n  ✅  Mentee '{name}' registered successfully! (ID: {mentee['id']})")


def calculate_average_rating(mentor):
    if not mentor["ratings"]:
        return 0.0
    return sum(mentor["ratings"]) / len(mentor["ratings"])


def match_mentor():
    print("\n" + "─" * 40)
    print("  🔍  MATCH A MENTOR")
    print("─" * 40)

    if not mentees:
        print("  ⚠️  No mentees registered yet. Please add a mentee first.")
        return

    if not mentors:
        print("  ⚠️  No mentors registered yet. Please add a mentor first.")
        return

    print("\n  Registered Mentees:")
    for m in mentees:
        print(f"    [{m['id']}] {m['name']} — Branch: {m['branch']}")

    mentee_id = input("\n  Enter Mentee ID to find a match: ").strip()

    selected_mentee = None
    for m in mentees:
        if str(m["id"]) == mentee_id:
            selected_mentee = m
            break

    if not selected_mentee:
        print("  ⚠️  Mentee ID not found.")
        return

    print(f"\n  Finding matches for: {selected_mentee['name']}")
    print(f"  Branch: {selected_mentee['branch']}")
    print(f"  Interests: {', '.join(selected_mentee['interests'])}")

    scored_mentors = []

    for mentor in mentors:
        score = 0

        if mentor["branch"] == selected_mentee["branch"]:
            score += 3

        for interest in selected_mentee["interests"]:
            if interest in mentor["interests"]:
                score += 1

        if score > 0:
            avg_rating = calculate_average_rating(mentor)
            scored_mentors.append({
                "mentor"    : mentor,
                "score"     : score,
                "avg_rating": avg_rating
            })

    if not scored_mentors:
        print("\n  😔  No suitable mentors found based on your branch and interests.")
        print("  💡  Tip: Try expanding your interests or wait for more mentors to join!")
        return

    scored_mentors.sort(key=lambda x: (x["score"], x["avg_rating"]), reverse=True)

    top_matches = scored_mentors[:3]

    print(f"\n  🏆  Top {len(top_matches)} Mentor Match(es) for {selected_mentee['name']}:")
    print("─" * 55)

    for rank, entry in enumerate(top_matches, start=1):
        m         = entry["mentor"]
        avg_r     = entry["avg_rating"]
        stars     = "⭐" * round(avg_r) if avg_r > 0 else "No ratings yet"
        interests = ", ".join(m["interests"])

        print(f"\n  #{rank}  {m['name']}  (ID: {m['id']})")
        print(f"       Branch    : {m['branch'].title()}")
        print(f"       Year      : {m['year']}")
        print(f"       Interests : {interests}")
        print(f"       Rating    : {stars}  ({avg_r:.1f} / 5.0)")
        print(f"       Contact   : {m['contact']}")
        print(f"       Match Score: {entry['score']} point(s)")

        print("\n" + "─" * 55)


def give_feedback():
    print("\n" + "─" * 40)
    print("  ⭐  GIVE FEEDBACK TO A MENTOR")
    print("─" * 40)

    if not mentors:
        print("  ⚠️  No mentors registered yet.")
        return

    print("\n  Registered Mentors:")
    for m in mentors:
        avg_r = calculate_average_rating(m)
        print(f"    [{m['id']}] {m['name']} — Avg Rating: {avg_r:.1f}/5.0")

    mentor_id = input("\n  Enter Mentor ID to give feedback: ").strip()

    selected_mentor = None
    for m in mentors:
        if str(m["id"]) == mentor_id:
            selected_mentor = m
            break

    if not selected_mentor:
        print("  ⚠️  Mentor ID not found.")
        return

    print(f"\n  Giving feedback for: {selected_mentor['name']}")

    while True:
        rating_input = input("  Rate this mentor (1 = Poor, 5 = Excellent): ").strip()
        if rating_input in ["1", "2", "3", "4", "5"]:
            rating = int(rating_input)
            break
        print("  ⚠️  Please enter a number between 1 and 5.")

    comment = input("  Leave a comment (or press Enter to skip): ").strip()

    selected_mentor["ratings"].append(rating)
    if comment:
        selected_mentor["feedback"].append(comment)

    new_avg = calculate_average_rating(selected_mentor)
    print(f"\n  ✅  Thank you for your feedback!")
    print(f"  {selected_mentor['name']}'s new average rating: {new_avg:.1f} / 5.0")


def view_all_mentors():
    print("\n" + "─" * 50)
    print("  📄  ALL REGISTERED MENTORS")
    print("─" * 50)

    if not mentors:
        print("  ⚠️  No mentors registered yet. Be the first!")
        return

    sorted_mentors = sorted(mentors, key=lambda m: calculate_average_rating(m), reverse=True)

    for index, m in enumerate(sorted_mentors):
        avg_r     = calculate_average_rating(m)
        stars     = "⭐" * round(avg_r) if avg_r > 0 else "—"
        interests = ", ".join(m["interests"])
        badge     = "  🏆 TOP MENTOR" if index == 0 and avg_r > 0 else ""

        print(f"\n  ID      : {m['id']}{badge}")
        print(f"  Name    : {m['name']}")
        print(f"  Branch  : {m['branch'].title()}")
        print(f"  Year    : {m['year']}")
        print(f"  Contact : {m['contact']}")
        print(f"  Interests: {interests}")
        print(f"  Rating  : {stars}  ({avg_r:.1f} / 5.0)  [{len(m['ratings'])} review(s)]")

        if m["feedback"]:
            print("  Reviews :")
            for fb in m["feedback"]:
                print(f"    💬 \"{fb}\"")

        print("  " + "·" * 45)


def main():
    display_banner()

    while True:
        display_menu()
        choice = input("  Enter your choice (1–6): ").strip()

        if choice == "1":
            add_mentor()

        elif choice == "2":
            add_mentee()

        elif choice == "3":
            match_mentor()

        elif choice == "4":
            give_feedback()

        elif choice == "5":
            view_all_mentors()

        elif choice == "6":
            print("\n" + "=" * 55)
            print("  👋  Thank you for using the Peer Mentorship Platform!")
            print("  🌟  Keep learning and keep growing. Goodbye!")
            print("=" * 55 + "\x