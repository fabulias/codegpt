build:
	@echo "[building image...]"
	@docker build -t codegpt-image .

run:
	@echo "[running app...]"
	@docker run -it --rm -p 8501:8501 --name codegpt-app codegpt-image