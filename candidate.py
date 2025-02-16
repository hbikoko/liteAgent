from uagents import Agent, Context
import random

# 1) Create the agent
mock_metrics_agent = Agent(
    name="mockInterviewAgent",
    seed="some_mock_seed",
    port=8100,
    endpoint=["http://localhost:8100/submit"]
)

#uAgent just to say an agent was used, not bc we needed it for a script like this

candidate_metrics = {
    "candidate_abc": {
        "volume": 72,
        "pacing": 85,
        "tone": 90
    }
}

# 3) Every 15 seconds, randomize & log the updated metrics
@mock_metrics_agent.on_interval(15)
async def auto_update_metrics(ctx: Context):
    for cand_id in candidate_metrics:
        candidate_metrics[cand_id] = {
            "relevance": random.randint(0, 100),
            "confidence": random.randint(0, 100),
            "tone": random.randint(0, 100)
        }
        ctx.logger.info(f"Updated metrics for {cand_id}: {candidate_metrics[cand_id]}")

if __name__ == "__main__":
    # 4) Run the agent
    mock_metrics_agent.run()
