import json
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, Column, Integer, String, SmallInteger, Enum, Date, DateTime, Text, ForeignKey
import enum
from helpers import get_db_engine


Base = declarative_base()


class SexEnum(enum.Enum):
    male = 1
    female = 2
    other = 3

class User(Base):
    __tablename__ = 'users'
    id                  = Column(Integer, primary_key=True)
    login_name          = Column(String(50))
    email               = Column(String(50))
    created             = Column(DateTime)
    pwhash              = Column(String(150))


class Student(Base):
    __tablename__ = 'students'
    id                  = Column(Integer, primary_key=True)
    first_name          = Column(String(50))
    last_name           = Column(String(50))
    email               = Column(String(50))
    gpg_key             = Column(Text)
    birthday            = Column(Date)
    created             = Column(DateTime)
    year                = Column(Enum(SexEnum))
    sex                 = Column(Enum(SexEnum))
    notes               = Column(Text)


class Course(Base):
    __tablename__ = 'courses'
    id                  = Column(Integer, primary_key=True)
    name                = Column(String(50))
    subject             = Column(String(50))
    notes               = Column(Text)

class Exam(Base):
    __tablename__ = 'exams'
    id                  = Column(Integer, primary_key=True)
    date                = Column(String(50))
    weight              = Column(SmallInteger)
    description         = Column(Text)
    mark_sequence_id    = Column(Integer, ForeignKey('mark_sequences.id'))
    rating_scale_id     = Column(Integer, ForeignKey('rating_scales.id'))

class ExamPart(Base):
    __tablename__ = 'exam_parts'
    id                  = Column(Integer, primary_key=True)
    max_points          = Column(SmallInteger)           # zero points means bonus
    weight              = Column(SmallInteger)
    student_id          = Column(Integer, ForeignKey('students.id'))
    mark_sequence_id    = Column(Integer, ForeignKey('mark_sequences.id'))
    rating_scale_id     = Column(Integer, ForeignKey('rating_scales.id'))

class Mark(Base):
    __tablename__ = 'marks'
    id                  = Column(Integer, primary_key=True)
    value               = Column(Float)
    mark_sequence_id    = Column(Integer, ForeignKey('mark_sequences.id'))
    student_id          = Column(Integer, ForeignKey('students.id'))


class MarkSequence(Base):
    __tablename__ = 'mark_sequences'
    id                          = Column(Integer, primary_key=True)
    weight                      = Column(SmallInteger)
    parent_mark_sequence_id     = Column(Integer, ForeignKey('mark_sequences.id'))
    course_id                   = Column(Integer, ForeignKey('courses.id'))

class RatingScale(Base):
    __tablename__ = 'rating_scales'
    id                  = Column(Integer, primary_key=True)
    name                = Column(String(50))
    description         = Column(Text)
    steps               = relationship("RatingScaleStep")

class RatingScaleStep(Base):
    __tablename__ = 'rating_scale_steps'
    id                  = Column(Integer, primary_key=True)
    name                = Column(String(50))
    description         = Column(Text)
    ratings_scale_id    = Column(Integer, ForeignKey('rating_scales.id'))


if __name__ == "__main__":
    from sqlalchemy import create_engine

    engine = get_db_engine()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
