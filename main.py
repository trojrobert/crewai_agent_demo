import sys
from datetime import datetime
from textwrap import dedent
from typing import List, Optional

from crewai import Crew, Process
from dotenv import load_dotenv

from agents import city_guide_agent, destination_analyst_agent, itinerary_planner_agent
from tasks import analyze_destination_task, city_guide_task, create_itinerary_task

load_dotenv()


def main(origin, cities, interests, date_range):

    # Initialize agents
    destination_analyst = destination_analyst_agent()
    city_guide = city_guide_agent()
    itinerary_planner = itinerary_planner_agent()

    # Create tasks for each stage of planning
    destination_task = analyze_destination_task(
        destination_analyst, origin, cities, interests, date_range
    )

    city_task = city_guide_task(city_guide, cities, interests, date_range)
    itinerary_task = create_itinerary_task(
        itinerary_planner, cities, interests, date_range
    )

    # Create and configure the crew
    crew = Crew(
        agents=[destination_analyst, city_guide, itinerary_planner],
        tasks=[destination_task, city_task, itinerary_task],
        process=Process.sequential,
        verbose=True,
    )

    result = crew.kickoff()
    return result


if __name__ == "__main__":
    print("## Welcome to Travel Planner Crew")
    print("-------------------------------")

    # Get origin location
    origin = input(
        dedent(
            """
        From where will you be traveling from? (city, country): """
        )
    ).strip()

    # Get destination cities
    cities = input(
        dedent(
            """
        What are the cities options you are interested in visiting?
        (comma-separated list): """
        )
    ).strip()

    # Get date range
    date_range = input(
        dedent(
            """
            What is the date range for your trip?
            (Format: YYYY-MM-DD to YYYY-MM-DD): """
        )
    ).strip()

    # Get traveler interests
    interests = input(
        dedent(
            """
        What are your interests and hobbies?
        (This helps us personalize your trip): """
        )
    ).strip()

    result = main(origin, cities, date_range, interests)

    if result:
        print("\n########################")
        print("## Your Travel Plan")
        print("########################\n")
        print(result)

        # Optionally save the result to a file
        with open("travel_plan.md", "w") as f:
            f.write(result)
        print("\nYour travel plan has been saved to 'travel_plan.md'")
