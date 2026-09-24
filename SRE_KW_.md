## Instructions: Classifying Incidents by Assignment Group

### Purpose

Assign each incident to the team best positioned to investigate and resolve it. Use the incident symptoms, affected service, and technical ownership rather than the reporter's location or the team that first noticed the issue.

### Classification steps

1. **Review the incident details**: confirm the impact, affected users or systems, start time, error messages, and recent changes.
2. **Identify the affected service or component**: use monitoring data, dependency maps, logs, and the service catalog.
3. **Match the component to its owning assignment group**: select the group responsible for operating and supporting that service.
4. **Check severity and scope**: follow the incident-management severity matrix; severity does not change the assignment group unless an escalation process requires it.
5. **Validate the assignment**: confirm the group has the required access and expertise. If ownership is unclear, assign to the designated triage or service-desk group and document the reason.
6. **Route and document**: record the evidence used, suspected component, assignment decision, and any handoff details in the incident.

### Assignment guidelines

| Incident indication | Assignment group |
| --- | --- |
| Application errors, failed deployments, or application performance issues | Application support team that owns the service |
| Host, operating system, compute, or virtualization failures | Infrastructure/Compute operations |
| Network connectivity, DNS, load balancer, or firewall issues | Network operations |
| Database availability, replication, or query performance issues | Database operations |
| Storage capacity, I/O, or backup failures | Storage/Backup operations |
| Identity, authentication, authorization, or access issues | Identity and Access Management |
| Security alerts, suspected compromise, or policy violations | Security operations |
| Monitoring, alerting, or observability platform failures | Monitoring/Observability team |
| Unknown impact or multiple services affected | Incident triage, then reassign after investigation |

### Handoff requirements

Before reassigning an incident, include:

- A concise summary of the observed problem and business impact.
- Evidence collected, including timestamps, alerts, logs, and error messages.
- Troubleshooting already performed and its results.
- The suspected service or component and the reason for the new assignment group.
- Any urgency, customer communication, or escalation requirements.

Do not assign an incident based solely on a keyword. If several groups may be involved, assign the group that owns the primary failing component and link or notify dependent teams as needed.
