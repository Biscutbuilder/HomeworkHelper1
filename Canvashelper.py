import asyncio
import desktop_notifier
import time
from desktop_notifier import DesktopNotifier, DEFAULT_SOUND
import canvasapi
from canvasapi import Canvas  
API_URL = "https://fergflor.instructure.com/"
API_KEY = '16687~tGYLZAx8mCztGFVx6HuFUE8aZe6eKGhcLF3aHDXwuVfGxTGLzYuCBhGRGtR6vA9J'

canvas = Canvas(API_URL, API_KEY)
canvas = Canvas(API_URL, API_KEY)


user = canvas.get_current_user()
print(f"Gathering unsubmitted items for: {user.name}\n")


courses = canvas.get_courses(enrollment_state="active", enrollment_type="student")


while True:
    for course in courses:
        print(f"Checking Class: {course.name}")
        

        unsubmitted_list = course.get_multiple_submissions(
            student_ids=[user.id], 
            workflow_state="unsubmitted"
        )
        

        has_unsubmitted = False
        for submission in unsubmitted_list:

            if hasattr(submission, 'assignment'):
                assignment_name = submission.assignment.get('name', 'Unnamed Assignment')
                due_date = submission.assignment.get('due_at', 'No Due Date')
                async def main(notifier):
                    await notifier.send(
                        title="Canvas Unsubmitted Items Checker",
                        message=f"Missing: {assignment_name} (Due: {due_date})",
                        sound=DEFAULT_SOUND
                    )
                if __name__ == "__main__":
                    notifier = DesktopNotifier()
                    asyncio.run(main(notifier))            
                print(f" Missing: {assignment_name} (Due: {due_date})")
                has_unsubmitted = True
                
        if not has_unsubmitted:
            print(" All caught up in this course!")
            async def main(notifier):
                await notifier.send(
                    title="Canvas Unsubmitted Items Checker",
                    message=f"All cought up in {course.name}",
                    sound=DEFAULT_SOUND
                    
            
            )
            time.sleep(10)

            if __name__ == "__main__":
                notifier = DesktopNotifier()
                asyncio.run(main(notifier))
    time.sleep(3*60*60)
    
