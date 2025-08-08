#!/usr/bin/env bash
set -eu
SPEC="$(basename "$(realpath "$(dirname "$0")")")"
VERSION=$(grep Version: "$SPEC.spec" | awk '{print $2}')

rm -f "$SPEC-$VERSION.tar.gz"
tar -czf "$SPEC-$VERSION.tar.gz" src
