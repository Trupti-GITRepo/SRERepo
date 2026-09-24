import os
from typing import Any

import requests


def get_incidents(
	instance: str,
	username: str,
	password: str,
	query: str = "",
	limit: int = 100,
) -> list[dict[str, Any]]:
	"""Return incidents from a ServiceNow instance using its Table API."""
	url = f"https://{instance}.service-now.com/api/now/table/incident"
	response = requests.get(
		url,
		auth=(username, password),
		headers={"Accept": "application/json"},
		params={"sysparm_query": query, "sysparm_limit": limit},
		timeout=30,
	)
	response.raise_for_status()
	return response.json().get("result", [])


if __name__ == "__main__":
	incidents = get_incidents(
		instance=os.environ["SERVICENOW_INSTANCE"],
		username=os.environ["SERVICENOW_USERNAME"],
		password=os.environ["SERVICENOW_PASSWORD"],
		query=os.getenv("SERVICENOW_QUERY", "ORDERBYDESCsys_created_on"),
		limit=int(os.getenv("SERVICENOW_LIMIT", "100")),
	)
	for incident in incidents:
		print(f'{incident.get("number")}: {incident.get("short_description")}')
