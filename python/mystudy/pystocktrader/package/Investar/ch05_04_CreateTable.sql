-- ch05_04_CreateTable.sql
CREATE TABLE IF NOT EXISTS company_info (
    code VARCHAR(20),
    company VARCHAR(40),
    last_update Date,
    PRIMARY KEY (code)
);

CREATE TABLE IF NOT EXISTS daily_price (
    code VARCHAR(20),
    date Date,
    open BIGINT(20),
    high BIGINT(20),
    low BIGINT(20),
    close BIGINT(20),
    diff BIGINT(20),
    volume BIGINT(20),
    PRIMARY KEY (code, date)
);