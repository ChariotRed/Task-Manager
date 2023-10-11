import schedule
import time
from datetime import datetime

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, time, task):
        """Add a task to the tasks dictionary."""
        if time in self.tasks:
            self.tasks[time].append(task)
        else:
            self.tasks[time] = [task]
        self._schedule_task(time, task)

    def _schedule_task(self, time, task):
        """Schedule the task."""
        schedule.every().day.at(time).do(self._notify, task=task)

    def _notify(self, task):
        """Function to print the task as a reminder."""
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"[{current_time}] Reminder: {task}")

    def run(self):
        """Keep running the task manager."""
        while True:
            schedule.run_pending()
            time.sleep(60)

# Usage
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("10:00", "Meeting with team.")
    manager.add_task("15:30", "Submit the report.")
    manager.run()
