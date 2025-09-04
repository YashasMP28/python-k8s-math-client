from kubernetes import client, config
import time
config.load_kube_config()

batch_v1 = client.BatchV1Api()

job_name = "math-job-client"
job = client.V1Job(
    api_version="batch/v1",
    kind="Job",
    metadata=client.V1ObjectMeta(name=job_name),
    spec=client.V1JobSpec(
        template=client.V1PodTemplateSpec(
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="math-container",
                        image="math-evaluator:1.1",
                        env=[client.V1EnvVar(name="MATH_EXPRESSION", value="20+5*3")]
                    )
                ],
                restart_policy="Never"
            )
        ),
        backoff_limit=2
    )
)

batch_v1.create_namespaced_job(body=job, namespace="default")
print("Job created. Waiting for completion...")

while True:
    job_status = batch_v1.read_namespaced_job_status(job_name, namespace="default")
    if job_status.status.succeeded == 1:
        break
    time.sleep(2)

from kubernetes.stream import stream
pods = client.CoreV1Api().list_namespaced_pod(namespace="default", label_selector=f"job-name={job_name}")
pod_name = pods.items[0].metadata.name

core_v1 = client.CoreV1Api()
logs = core_v1.read_namespaced_pod_log(name=pod_name, namespace="default")
print("Job Logs:\n", logs)
