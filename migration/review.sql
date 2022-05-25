CREATE TABLE review (
	review_id VARCHAR(255),
	user_id VARCHAR(255),
	business_id VARCHAR(255),
	stars NUMERIC,
	useful INT,
	funny INT,
	cool INT,
	text VARCHAR(20000),
	date_review DATE,
	text_tip VARCHAR(20000),
	compliment_count INT
)